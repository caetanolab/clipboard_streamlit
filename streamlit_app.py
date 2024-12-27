import streamlit as st
from streamlit.components.v1 import html

js = """
<button id="copyButton">Copy Image and Text</button>
<script>



async function copyImageAndText(imageUrl, text) {
    const queryOpts = { name: 'clipboard-write', allowWithoutGesture: false };
    const permissionStatus = await navigator.permissions.query(queryOpts);
    
    // Listen for changes to the permission state
    permissionStatus.onchange = async () => {
      alert(permissionStatus.state);
    }

    try {
        // Fetch the image and create a blob
        const response = await fetch(imageUrl);
        const blob = await response.blob();

        // Create an image item for the clipboard

        // Write image to clipboard
        await navigator.clipboard.write([
            new ClipboardItem({[blob.type]: blob}),
            new ClipboardItem({"text/plain": "streamlit"})
        ]);

        alert("Image and text copied to clipboard!");
    } catch (error) {
        alert(error);
    }
}

document.getElementById("copyButton").addEventListener("click", () => {
    const imageUrl = parent.document.images[0].src;
    const text = "Sample text to copy";
    copyImageAndText(imageUrl, text);
});

</script>

"""

if picture := st.file_uploader(
        'Take a picture or upload an image to start',
        type=['png', 'jpg']):

    st.image(picture)

    html(js)