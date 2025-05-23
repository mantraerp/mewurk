app_name = "mewurk"
app_title = "Mewurk"
app_publisher = "Mantra"
app_description = "Mewurk"
app_email = "info@mantratec.com"
app_license = "mit"

fixtures = [
    "Workflow",
    "Workflow State",
    "Workflow Action Master",
    "Letter Head",
    "Role",
    "Custom DocPerm",
    {"dt": "Report", "filters": [["module", "in", ["mewurk"]]]},
    {"dt": "Print Format", "filters": [["module", "in", ["mewurk"]]]},
    {"dt": "Server Script", "filters": [["module", "in", ["mewurk"]]]},
    {"dt": "Client Script", "filters": [["module", "in", ["mewurk"]]]},
    {"dt": "Property Setter", "filters": [["module", "in", ["mewurk"]]]}
]