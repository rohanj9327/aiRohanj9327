from asyncio import graph
from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class BMIState(TypedDict):
    weight_kg: float
    height_m: float
    bmi: float


def caclulate_bmi(state: BMIState) -> BMIState:
    weight = state['weight_kg']
    height = state['height_m']
    bmi = weight/(height**2)

    state['bmi'] = round(bmi, 2)

    print(state)
    return state

def label_bmi(state: BMIState) -> BMIState:
    bmi = state['bmi']

    if bmi < 18.5:
        state["category"] = "Underweight"
    elif 18.5 <= bmi < 25:
        state["category"] = "Normal"
    elif 25 <= bmi < 30:
        state["category"] = "Overweight"
    else:
        state["category"] = "Obese"
    print(state)
    return state

graph = StateGraph(BMIState)

graph.add_node("calculate_bmi", caclulate_bmi)
graph.add_node("label_bmi", label_bmi)

graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', 'label_bmi')
graph.add_edge('label_bmi', END)

workflow = graph.compile()

# Save the graph diagram as a PNG image file
#png_bytes = workflow.get_graph().draw_mermaid_png()
#with open("bmi_graph.png", "wb") as f:
#   f.write(png_bytes)

print(workflow.get_graph().draw_ascii())

initial_state = {'weight_kg' : 79, 'height_m': 1.65, 'category': ''}
workflow.invoke(initial_state)