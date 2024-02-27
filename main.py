import gradio as gr
import os

# set the directory where the images are located
IMAGES_DIR = '.'


def get_image_paths():
    files = os.listdir(IMAGES_DIR)
    # sort files by filename
    files.sort()
    # check for png or jpg files
    images_list = [os.path.join(IMAGES_DIR, file) for file in files if file.lower().endswith('.png')
                   or file.lower().endswith('.jpg')]
    # output the list of images
    print(f'Found {len(images_list)} images.')
    return images_list


def delete_image(image_index):
    print(f'Delete image: {image_index}')
    if image_index > 0:
        path = os.path.join(IMAGES_DIR, get_image_paths()[image_index])
        os.remove(path)
        index.value = image_index - 1
    else:
        path = 'No image to delete.'
    return path, get_image_paths(), image_index


def image_selected(sel: gr.SelectData):
    print(f'Image selected: {sel.index}')
    return sel.index, sel.value['image']['orig_name']


if __name__ == "__main__":
    initial = get_image_paths()
    with gr.Blocks() as gallery:
        with gr.Row():
            gal = gr.Gallery(show_label=True, value=initial)
        with gr.Row():
            update = gr.Button("Update")
            delete = gr.Button("Delete")
        with gr.Row():
            index = gr.Number(0, label='Index')
            output = gr.Text(label='Filename')

        update.click(get_image_paths, None, outputs=[gal])
        gal.select(image_selected, outputs=[index, output])
        delete.click(fn=delete_image, inputs=[index], outputs=[output, gal, index])

    gallery.launch(server_name='0.0.0.0', share=True)
