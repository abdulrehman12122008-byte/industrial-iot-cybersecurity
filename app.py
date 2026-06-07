import gradio as gr

def assess_risk(devices, encryption, firewall, password_strength):
    risk = 100
    risk -= devices * 2

    if encryption == "Yes":
        risk -= 20
    if firewall == "Yes":
        risk -= 20

    if password_strength == "Strong":
        risk -= 30
    elif password_strength == "Medium":
        risk -= 15

    risk = max(0, min(100, risk))

    if risk > 70:
        level = "High Risk"
    elif risk > 40:
        level = "Medium Risk"
    else:
        level = "Low Risk"

    return risk, level

demo = gr.Interface(
    fn=assess_risk,
    inputs=[
        gr.Slider(1, 50, value=10, label="Number of IIoT Devices"),
        gr.Radio(["Yes", "No"], label="Encryption Enabled"),
        gr.Radio(["Yes", "No"], label="Firewall Installed"),
        gr.Radio(["Weak", "Medium", "Strong"], label="Password Strength")
    ],
    outputs=[
        gr.Textbox(label="Risk Score"),
        gr.Textbox(label="Threat Level")
    ],
    title="Industrial IoT Cybersecurity Analyzer",
    description="Developed By: 25-ME-151, 25-ME-155, 25-ME-159"
)

demo.launch()
