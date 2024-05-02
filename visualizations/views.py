from django.shortcuts import render

how_to = {
    "homepage": {"about_this_page": """This page is for those who enjoy the technical graphics and driver performance analyses and comparisons during the Formula 1 race weekend coverage on f1.tv.

                 Analysts like Sam Collins have access to some great tools for analysis, including a handful of great charts.
                 This website will allow you to recreate those charts, and explore the graphics interactively, for any Formula 1 Session available through fastf1.""",
                 "getting_started": """Follow the Choose Session link above to select your session of interest, and submit your search. The data will load on the backend, and that data will be available to explore with any of the data visualizations listed."""
                 },
    "plot_list": ['Position Changes During a Race',
                  'Overlying Speed Traces',
                  'Driver Laptimes Scatterplot',
                  'Gearshifts',
                  'Team Pace Comparison'
                  ],
    "choose_a_session": """Use the dropdown menus to select a year, a race weenend (formatted like 'round 1: australia') and a session like FP1, or Qualifying, or Sprint Race,
    depending on what sessions were available at the race that year (example: only whatever sessions are available, so figure out how to get that out of fastf1 data once year and race weekend are selected), 
    and submit to load the data.

    Choose from the available plots to explore the data."""
}


def homepage(request):
    # on the otherside, textdata will be a dict, so accesss textdata.about_this_page and textdata.getting_started
    textdata = how_to["homepage"]
    return render(request, "visualizations/homepage.html", {
        "textdata": textdata
    })


def choose_session(request):
    # on the otherside, textdata will be a string, so access textdata directly as text
    textdata = how_to["choose_a_session"]
    return render(request, "visualizations/choose_session.html", {
        "textdata": textdata
    })


def plot_list(request):
    # on the otherside, textdata will be a list, so access textdata in a for loop, like for plot in textdata...
    textdata = how_to["plot_list"]
    return render(request, "visualizations/plot_list.html", {
        "textdata": textdata
    })
