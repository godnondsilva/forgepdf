import os, shutil
from datetime import datetime
from pathlib import Path
from app.store import state, states

# Function to move a file to the downloads folder
def move_to_downloads(save_type):
        # If ForgePDF folder doesn't exist in downloads folder, creating it
        if not os.path.exists(os.path.join(Path.home(), "Downloads", "ForgePDF")):
                os.mkdir(os.path.join(Path.home(), "Downloads", "ForgePDF"))
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads/ForgePDF/"))
        date = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
        new_name = 'forgepdf_' + save_type + '_' + date + '.pdf'
        shutil.move('output.pdf', path_to_download_folder+new_name)
        if len(state.get_state(states.PREVIEW_PDFS)) < 5:
                state.set_state(states.PREVIEW_PDFS, state.get_state(states.PREVIEW_PDFS) + [new_name])
        else:
                state.set_state(states.PREVIEW_PDFS, state.get_state(states.PREVIEW_PDFS)[1:] + [new_name])
        open_folder(new_name)

# Function to open folder of a file
def open_folder(filename):
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads/ForgePDF/"))
        os.startfile(path_to_download_folder)