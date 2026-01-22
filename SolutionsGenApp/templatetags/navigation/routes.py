# Description: This file contains the custom template tag to render the navigation links.
from django import template
from django.urls import reverse

# Register the template tag
register = template.Library()

# Define the template tag
@register.inclusion_tag("navigation/navlink.html", takes_context=True)
def render_routes(context):
    request = context.get('request')
    routes = [
        {
            'url': 'SolutionsGenApp:home',
            'name': 'Home',
        },
        {
            'url': 'SolutionsGenApp:projects',
            'name': 'Projects',
        },
        {
            'url': 'SolutionsGenApp:services',
            'name': 'Services',
        },
        {
            'url': 'SolutionsGenApp:about-us',
            'name': 'About Us',
        }
    ]

    current_path = request.path if request else None


    for route in routes:
        route['active'] = reverse(route['url']) == current_path
        print(f"Route: {route['name']}, URL: {reverse(route['url'])}, Active: {route['active']}")

    context['routes'] = routes
    return context
