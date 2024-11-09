import os

def generate_invitations(template, attendees):
    # Checks if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Checks if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Logs an error and stops if template or attendees is empty
    if not template:
        print("Template is empty, no files generated.")
        return
    if not attendees:
        print("No data provided, no files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        try:
            # Replace placeholders with actual values or "N/A" if data is missing
            content = template
            content = content.replace("{name}", attendee.get("name", "N/A"))
            content = content.replace("{event_title}", attendee.get("event_title", "N/A"))
            content = content.replace("{event_date}", attendee.get("event_date") or "N/A")
            content = content.replace("{event_location}", attendee.get("event_location", "N/A"))

            # Create output file name
            output_filename = f"output_{index}.txt"

            # Check if the file already exists
            if os.path.exists(output_filename):
                print(f"The file '{output_filename}' already exists. It will not be overwritten.")
                continue

            # Write to the file
            with open(output_filename, "w") as file:
                file.write(content)
                print(f"Invitation successfully written to '{output_filename}'.")

        except Exception as e:
            print(f"Error: An error occurred while generating '{output_filename}': {e}")
