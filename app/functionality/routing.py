from app.store import state, states
from app import home, encryptpdf, decryptpdf, splitpdf, mergepdf

def route_frame(window, location):
    # Guard before going to the next frame
    if location == state.get_state(states.CURRENT_FRAME):
        return

    if location == "home":
        state.set_state(states.CURRENT_FRAME, "home")
        home.load_home(window)

    if location == "encryptpdf":
        state.set_state(states.CURRENT_FRAME, "encryptpdf")
        encryptpdf.load_encrypt_pdf(window)

    if location == "decryptpdf":
        state.set_state(states.CURRENT_FRAME, "decryptpdf")
        decryptpdf.load_decrypt_pdf(window)

    if location == "splitpdf":
        state.set_state(states.CURRENT_FRAME, "splitpdf")
        splitpdf.load_split_pdf(window)

    if location == "mergepdf":
        state.set_state(states.CURRENT_FRAME, "mergepdf")
        mergepdf.load_merge_pdf(window)