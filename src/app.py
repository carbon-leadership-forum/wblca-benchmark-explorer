from dash import Dash, html, page_container, dcc, State
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from src.components.header import create_header

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    routing_callback_inputs={
        # The app state is serialised in the URL hash without refreshing the page
        # This URL can be copied and then parsed on page load
        "state": State("main-url", "hash"),
    },
)
server = app.server

load_figure_template("bootstrap")

header = create_header()

app.layout = dbc.Container(
    [
        dcc.Store(
            id="byob_data",
            storage_type="memory",
        ),
        dcc.Location(id="main-url"),
        dbc.Row(
            [
                html.Header(
                    dbc.Row(
                        dbc.Col(
                            header,
                            className="mb-2",
                            xs=12,
                            sm=12,
                            md=12,
                            lg=12,
                            xl=10,
                            xxl=10,
                        ),
                        justify="center",
                    ),
                ),
            ]
        ),
        dbc.Row(page_container),
    ],
    fluid=True,
    className="dbc",
)

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-KMWHP8B0DJ"></script>
        <script>window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());

gtag('config', 'G-KMWHP8B0DJ');
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%scripts%}
            {%config%}
            {%renderer%}
        </footer>
    </body>
</html>"""


if __name__ == "__main__":
    app.run(debug=True)
