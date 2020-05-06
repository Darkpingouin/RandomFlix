import json
import RandomFlix

import ask_sdk_core as Alexa
from ask_sdk_model.interfaces.alexa.presentation.apl import (
    RenderDocumentDirective, ExecuteCommandsDirective, SpeakItemCommand, HighlightMode
)
from ask_sdk_core.utils import (get_supported_interfaces)


def _load_apl_document(file_path):
    """
    Load the apl json document at the path into a dict object
    """
    with open(file_path) as f:
        return json.load(f)


APL_DOCS = {
    'main': _load_apl_document('./apl/template.json'),
    'home': _load_apl_document('./apl/home.json')
}


def supports_apl(handler_input):
    """
    Checks whether APL is supported by the User's device
    """
    print(handler_input)
    supported_interfaces = get_supported_interfaces(
        handler_input)
    return supported_interfaces.alexa_presentation_apl != None


def launch_screen(handler_input, movie):
    """
    Adds Launch Screen (APL Template) to Response
    """
    # Only add APL directive if User's device supports APL
    if(supports_apl(handler_input)):
        print("I'm in")
        handler_input.response_builder.add_directive(
            RenderDocumentDirective(
                token="launchToken",
                document=APL_DOCS['main'],
                datasources=generateLaunchScreenDatasource(handler_input, movie)
            )
        )


def homeScreen(handler_input):
    """
    Adds Help Screen (APL Template) to Response
    """
    # Only add APL directive if User's device supports APL
    if(supports_apl(handler_input)):
        handler_input.response_builder.add_directive(
            RenderDocumentDirective(
                token="helpScreen",
                document=APL_DOCS['home']
            )
        )


def generateLaunchScreenDatasource(handler_input, movie):
    """
    Compute the JSON Datasource associated to APL Launch Screen
    """

    # Generate JSON Datasource
    return {
        'RandomFlixData': {
            'type': 'object',
            'properties': {
                'headerTitle': movie.title,
                'description': movie.description,
                'img': movie.image,
            }
        }
    }


