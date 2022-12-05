import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

try:
    sys.path.remove(str(parent))
except ValueError:  # Already removed
    pass

import streamlit as st

VERSION = ".".join(st.__version__.split(".")[:2])

from demos import orchestrator

demo_pages = {
    "st.camera_input": orchestrator.show_examples,
}



contributors = []

intro = f"""
This release launches Camera Input as well as other improvements and bug fixes.
"""

release_notes = f"""
---
**Highlights**

- 📸 Introducing `st.camera_input` for uploading images straight from your camera.

**Notable Changes**

- 🚦 Widgets now have the `disabled` parameter that removes interactivity.
- 🚮 Clear `st.experimental_memo` and `st.experimental_singleton` programmatically by using the `clear()` method on a cached function.
- 📨 Developers can now configure the maximum size of a message to accommodate larger messages within the Streamlit application. See `server.maxMessageSize`.
- 🐍 We formally added support for Python 3.10.

**Other Changes**

- 😵‍💫 Calling `str` or `repr` on `threading.current_thread()` does not cause a RecursionError ([#4172](https://github.com/streamlit/streamlit/issues/4172)).
- 📹 Gracefully stop screencast recording when user removes permission to record ([#4180](https://github.com/streamlit/streamlit/pull/4180)).
- 🌇 Better scale images by using a higher-quality image bilinear resampling algorithm ([#4159](https://github.com/streamlit/streamlit/pull/4159)).

[Click here](https://github.com/streamlit/streamlit/compare/1.3.0...1.4.0) to check out all updates. As always, thank you to all [our contributors](https://github.com/streamlit/streamlit/graphs/contributors) who help make Streamlit awesome!
"""

# End release updates


def draw_main_page():
    st.write(
        f"""
        # Welcome to Streamlit 1.4.0! 👋
        """
    )

    st.write(orchestrator.show_examples)


# Draw sidebar
pages = list(demo_pages.keys())


pages.insert(0, "Release Notes")
st.sidebar.title(f"Streamlit v1.4.0 🎈")
query_params = st.experimental_get_query_params()
index = 1
# selected_demo = st.sidebar.radio("", pages, index, key="pages")

demo_pages["st.camera_input"]()
