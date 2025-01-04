from dotenv import load_dotenv
import os
from notion_client import Client

# Load environment variables
load_dotenv()
notion_token = os.getenv("NOTION_TOKEN")
# Initialize the Notion client
notion = Client(auth=notion_token)

def append_to_notion_page(page_id, content):
    """
    Append a story to a Notion page.

    Args:
        page_id (str): The ID of the Notion page.
        content (str): The story content to append.
    """
    try:
        # Append new content as a block to the page
        notion.blocks.children.append(
            block_id=page_id,
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": content
                                }
                            }
                        ]
                    }
                }
            ]
        )
        print("Content appended to the page successfully.")
    except Exception as e:
        print(f"Error appending content to the page: {e}")

# Example usage
page_id = "171543a018f48054aaa1cee8a6d32b5f"  # Replace with your actual page ID
story_content = "Once upon a time, in a world powered by AI, there was a story waiting to be told..."
append_to_notion_page(page_id, story_content)