from dotenv import load_dotenv
import os
from array import array
from PIL import Image, ImageDraw
import sys
import time
from matplotlib import pyplot as plt
import numpy as np

# Import namespaces
import azure.ai.vision as sdk


def main():
    global cv_client

    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Get image
        image_file = 'images/people.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Authenticate Azure AI Vision client
        cv_client = sdk.VisionServiceOptions(ai_endpoint, ai_key)
        
        # Analyze image
        AnalyzeImage(image_file, cv_client)

    except Exception as ex:
        print(ex)


def AnalyzeImage(image_file, cv_client):
    print('\nAnalyzing', image_file)

    # Specify features to be retrieved (PEOPLE)
    analysis_options = sdk.ImageAnalysisOptions()
        
    features = analysis_options.features = (
        sdk.ImageAnalysisFeature.PEOPLE
    )    

    # Get image analysis


if __name__ == "__main__":
    main()