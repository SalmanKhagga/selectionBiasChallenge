import numpy as np
import matplotlib.pyplot as plt

def create_statistics_meme(original_img, stipple_img, block_letter_img, masked_stipple_img, output_path, dpi=150, background_color="white"):
    fig = plt.figure(figsize=(16, 5), facecolor=background_color)
    panels = [
        (original_img, "Reality"),
        (stipple_img, "Your Model"),
        (block_letter_img, "Selection Bias"),
        (masked_stipple_img, "Estimate\n('seems legit')"),
    ]
    for i, (img, label) in enumerate(panels):
        ax = fig.add_subplot(1, 4, i + 1)
        ax.imshow(img, cmap='gray', vmin=0, vmax=1)
        ax.axis('off')
        ax.set_title(label, fontsize=13, fontweight='bold', pad=8)
    plt.tight_layout(pad=1.5)
    plt.savefig(output_path, dpi=dpi, bbox_inches='tight', facecolor=background_color)
    plt.close()
    