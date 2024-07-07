"""
TODOs:

- [ ] Add chart view
- [ ] Add chart edit view
- [ ] Add chart delete view
- [ ] Add other chart types
- [ ] Switch to Python charting library once I am where I can pip install

STRETCH GOALS
- [ ] Pull data from external source(s)
- [ ] Add chart search feature
- [ ] JS Animated chart for wow factor
"""


import json
from pathlib import Path
import uvicorn
from fasthtml.common import *


app = FastHTML(hdrs=(
    picolink,
    Script(src="https://cdn.plot.ly/plotly-2.32.0.min.js"),
))


@app.get('/')
def home():
    charts = Path('charts/').rglob('*.json')

    chart_links = []
    for chart in charts:
        data = json.loads(chart.read_text())
        name = f"{data['title']} ({data['type']})"
        chart_links.append(Li(A(name, href=f"/{chart.stem}"), Br(), Small(data.get("description"))))

    return (
            Header(H1('Super Dashboard'), cls="container"),
            Main(
                Ul(
                *chart_links,
                ),
                cls="container"
            )
    )


@app.get('/{slug}')
def chart(slug: str):
    chart = json.loads(Path(f'charts/{slug}.json').read_text())

    return (
        Header(H1('Super Dashboard'), cls="container"),
        Main(
            P(chart.get("title")),
            P(Small(chart.get("description"))),
            Div(id="myDiv"), cls="container"),
        # TODO - Maybe replace this with plotly.py
        Script(f"var data = {chart.get('data', [])}; Plotly.newPlot('myDiv', data);")
    )


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", default=8000)))    