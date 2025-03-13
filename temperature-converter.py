from nicegui import ui

ui.colors(
      primary='#003973',
      secondary='#26A69A',
      accent='#280061',
      positive='#22b5e6',
      negative='#C10015',
      info='#8aebff',
      warning='#F2C037'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-2xl font-semibold text-positive mt-4")
        # text-positive: sets the color of the text to defined positive color
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-2xl font-semibold text-negative mt-4")
        # text-negative: sets the color of the text to defined negative color

with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl bg-gray-100"):
    # w-100: Set element width to be fixed at 100
    # p-6: adds a padding of 24 pixels to the element
    # shadow-xl: applies a extra-large shadow box to the element
    # mx-auto: centers the element horizontally
    # mt-10: adds a top margin of 40 pixels
    # rounded-xl: applies a extra-large border radies for rounded corners 
    ui.label("Temperature Converter").classes("text-3xl font-bold font-sans text-accent mb-4")
    # text-2xl: sets text size to 24 pixels
    # font-bold: makes the text/font bold
    # text-accent: set the color of text to the defined accent color
    # mb-4: adds a bottom margin of 16 pixels
    input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full h-fit mb-4 p-2 text-lg border rounded")
    input_slider = ui.slider(min=-200, max=200, value=0)
    input_field.bind_value_from(input_slider, 'value')
    input_slider.bind_value_from(input_field, 'value')

    # w-full: sets the width of the element to 100% of its parent container
    # border: applies a default border of 1 pixel around the element
    # rounded: gives the element rounded corners
    conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4 text-xl")
    convert_button = ui.button("Convert", on_click=convert).classes("mx-auto text-white font-bold font-sans py-2 px-4 rounded")
    # text-white: sets the text color to white
    # py-2: adds a vertical padding of 8 pixels 
    # px-4: adds a horizontal padding of 16 pixels
    result_label = ui.label("").classes("text-lg mt-4")
   

ui.run()