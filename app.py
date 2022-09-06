import streamlit as st

st.title("Label Visibility Demo")


slider_visibility = st.radio(
    "Choose label visibility",
    ["visible", "hidden", "collapsed"],
    horizontal=True,
    key="slider",
)

if slider_visibility == "visible":
    m = st.slider("SLIDER_LABEL_M", value=42)
    n = st.slider("SLIDER_LABEL_N", value=64)
elif slider_visibility == "hidden":
    m = st.slider("SLIDER_LABEL_M", value=42, label_visibility="hidden")
    n = st.slider("SLIDER_LABEL_N", value=64, label_visibility="hidden")
elif slider_visibility == "collapsed":
    m = st.slider("SLIDER_LABEL_M", value=42, label_visibility="collapsed")
    n = st.slider("SLIDER_LABEL_N", value=64, label_visibility="collapsed")

st.write("m =", m)
st.write("n =", n)

with st.expander("RADIO"):

    radio_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="radio",
    )

    if radio_visibility == "visible":
        a = st.radio("LABEL_A", ["apple", "banana", "apricot"], help="HELP!")
        b = st.radio("LABEL_B", ["apple", "banana", "apricot"], help="HELP!")
        c = st.radio("LABEL_C", ["apple", "banana", "apricot"], help="HELP!")
    elif radio_visibility == "hidden":
        a = st.radio(
            "LABEL_A",
            ["apple", "banana", "apricot"],
            label_visibility="hidden",
            help="HELP!",
        )
        b = st.radio(
            "LABEL_B",
            ["apple", "banana", "apricot"],
            label_visibility="hidden",
            help="HELP!",
        )
        c = st.radio(
            "LABEL_C",
            ["apple", "banana", "apricot"],
            label_visibility="hidden",
            help="HELP!",
        )
    elif radio_visibility == "collapsed":
        a = st.radio(
            "LABEL_A",
            ["apple", "banana", "apricot"],
            label_visibility="collapsed",
            help="HELP!",
        )
        b = st.radio(
            "LABEL_B",
            ["apple", "banana", "apricot"],
            label_visibility="collapsed",
            help="HELP!",
        )
        c = st.radio(
            "LABEL_C",
            ["apple", "banana", "apricot"],
            label_visibility="collapsed",
            help="HELP!",
        )


with st.expander("TIME INPUT"):

    time_input_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="time_visibility",
    )

    if time_input_visibility == "visible":
        m = st.time_input("TIME_INPUT_LABEL_M")
        n = st.time_input("TIME_INPUT_LABEL_N")
    elif time_input_visibility == "hidden":
        m = st.time_input("TIME_INPUT_LABEL_M", label_visibility="hidden")
        n = st.time_input("TIME_INPUT_LABEL_N", label_visibility="hidden")
    elif time_input_visibility == "collapsed":
        m = st.time_input("TIME_INPUT_LABEL_M", label_visibility="collapsed")
        n = st.time_input("TIME_INPUT_LABEL_N", label_visibility="collapsed")

with st.expander("COLOR INPUT"):

    color_picker_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="color_picker",
    )

    if color_picker_visibility == "visible":
        m = st.color_picker("COLOR_PICKER_LABEL_M")
        n = st.color_picker("COLOR_PICKER_LABEL_N")
    elif color_picker_visibility == "hidden":
        m = st.color_picker("COLOR_PICKER_LABEL_M", label_visibility="hidden")
        n = st.color_picker("COLOR_PICKER_LABEL_N", label_visibility="hidden")
    elif color_picker_visibility == "collapsed":
        m = st.color_picker("COLOR_PICKER_LABEL_M", label_visibility="collapsed")
        n = st.color_picker("COLOR_PICKER_LABEL_N", label_visibility="collapsed")


with st.expander("CAMERA INPUT"):
    camera_input_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="camera_input",
    )

    if camera_input_visibility == "visible":
        m = st.camera_input("CAMERA_INPUT_LABEL_M")
        n = st.camera_input("CAMERA_INPUT_LABEL_N")
    elif camera_input_visibility == "hidden":
        m = st.camera_input("CAMERA_INPUT_LABEL_M", label_visibility="hidden")
        n = st.camera_input("CAMERA_INPUT_LABEL_N", label_visibility="hidden")
    elif camera_input_visibility == "collapsed":
        m = st.camera_input("CAMERA_INPUT_LABEL_M", label_visibility="collapsed")
        n = st.camera_input("CAMERA_INPUT_LABEL_N", label_visibility="collapsed")

with st.expander("FILE UPLOADER"):
    file_uploader_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="file_uploader",
    )

    if file_uploader_visibility == "visible":
        m = st.file_uploader("CAMERA_INPUT_LABEL_M")
        n = st.file_uploader("CAMERA_INPUT_LABEL_N")
    elif file_uploader_visibility == "hidden":
        m = st.file_uploader("CAMERA_INPUT_LABEL_M", label_visibility="hidden")
        n = st.file_uploader("CAMERA_INPUT_LABEL_N", label_visibility="hidden")
    elif file_uploader_visibility == "collapsed":
        m = st.file_uploader("CAMERA_INPUT_LABEL_M", label_visibility="collapsed")
        n = st.file_uploader("CAMERA_INPUT_LABEL_N", label_visibility="collapsed")

with st.expander("MULTISELECT"):

    multiselect_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="multiselect",
    )

    if multiselect_visibility == "visible":
        m = st.multiselect("MULTISELECT_INPUT_LABEL_M", ["a", "b"])
        n = st.multiselect("MULTISELECT_INPUT_LABEL_N", ["a", "b"])
    elif multiselect_visibility == "hidden":
        m = st.multiselect(
            "MULTISELECT_INPUT_LABEL_M", ["a", "b"], label_visibility="hidden"
        )
        n = st.multiselect(
            "MULTISELECT_INPUT_LABEL_N", ["a", "b"], label_visibility="hidden"
        )
    elif multiselect_visibility == "collapsed":
        m = st.multiselect(
            "MULTISELECT_INPUT_LABEL_M", ["a", "b"], label_visibility="collapsed"
        )
        n = st.multiselect(
            "MULTISELECT_INPUT_LABEL_N", ["a", "b"], label_visibility="collapsed"
        )

with st.expander("SELECTBOX"):

    selectbox_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="selectbox",
    )

    if selectbox_visibility == "visible":
        m = st.selectbox("SELECTBOX_LABEL_M", ["a", "b"])
        n = st.selectbox("SELECTBOX_LABEL_N", ["a", "b"])
    elif selectbox_visibility == "hidden":
        m = st.selectbox("SELECTBOX_LABEL_M", ["a", "b"], label_visibility="hidden")
        n = st.selectbox("SELECTBOX_LABEL_N", ["a", "b"], label_visibility="hidden")
    elif selectbox_visibility == "collapsed":
        m = st.selectbox("SELECTBOX_LABEL_M", ["a", "b"], label_visibility="collapsed")
        n = st.selectbox("SELECTBOX_LABEL_N", ["a", "b"], label_visibility="collapsed")

with st.expander("NUMBER INPUT"):

    number_input_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="number_input",
    )

    if number_input_visibility == "visible":
        m = st.number_input("NUMBER_INPUT_LABEL_M")
        n = st.number_input("NUMBER_INPUT_LABEL_N")
    elif number_input_visibility == "hidden":
        m = st.number_input("NUMBER_INPUT_LABEL_M", label_visibility="hidden")
        n = st.number_input("NUMBER_INPUT_LABEL_N", label_visibility="hidden")
    elif number_input_visibility == "collapsed":
        m = st.number_input("NUMBER_INPUT_LABEL_M", label_visibility="collapsed")
        n = st.number_input("NUMBER_INPUT_LABEL_N", label_visibility="collapsed")

with st.expander("TEXT INPUT"):

    text_input_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="text_input",
    )

    if text_input_visibility == "visible":
        m = st.text_input("TEXT_INPUT_LABEL_M")
        n = st.text_input("TEXT_INPUT_LABEL_N")
    elif text_input_visibility == "hidden":
        m = st.text_input("TEXT_INPUT_LABEL_M", label_visibility="hidden")
        n = st.text_input("TEXT_INPUT_LABEL_N", label_visibility="hidden")
    elif text_input_visibility == "collapsed":
        m = st.text_input("TEXT_INPUT_LABEL_M", label_visibility="collapsed")
        n = st.text_input("TEXT_INPUT_LABEL_N", label_visibility="collapsed")

with st.expander("TEXT AREA"):

    text_area_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="text_area",
    )

    if text_area_visibility == "visible":
        m = st.text_area("TEXT_AREA_LABEL_M")
        n = st.text_area("TEXT_AREA_LABEL_N")
    elif text_area_visibility == "hidden":
        m = st.text_area("TEXT_AREA_LABEL_M", label_visibility="hidden")
        n = st.text_area("TEXT_AREA_LABEL_N", label_visibility="hidden")
    elif text_area_visibility == "collapsed":
        m = st.text_area("TEXT_AREA_LABEL_M", label_visibility="collapsed")
        n = st.text_area("TEXT_AREA_LABEL_N", label_visibility="collapsed")

with st.expander("SELECT SLIDER"):
    select_slider_visibility = st.radio(
        "Choose label visibility",
        ["visible", "hidden", "collapsed"],
        horizontal=True,
        key="select_slider",
    )

    if select_slider_visibility == "visible":
        m = st.select_slider("SELECT_SLIDER_LABEL_M", ["apple", "banana", "apricot"])
        n = st.select_slider("SELECT_SLIDER_LABEL_N", ["apple", "banana", "apricot"])
    elif select_slider_visibility == "hidden":
        m = st.select_slider(
            "SELECT_SLIDER_LABEL_M",
            ["apple", "banana", "apricot"],
            label_visibility="hidden",
        )
        n = st.select_slider(
            "SELECT_SLIDER_LABEL_N",
            ["apple", "banana", "apricot"],
            label_visibility="hidden",
        )
    elif select_slider_visibility == "collapsed":
        m = st.select_slider(
            "SELECT_SLIDER_LABEL_M",
            ["apple", "banana", "apricot"],
            label_visibility="collapsed",
        )
        n = st.select_slider(
            "SELECT_SLIDER_LABEL_N",
            ["apple", "banana", "apricot"],
            label_visibility="collapsed",
        )
