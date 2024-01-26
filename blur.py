from PIL import Image, ImageFilter
import os

def blur_images(input_folder, output_folder, blur_radius):
    # Membuat folder output jika belum ada
    os.makedirs(output_folder, exist_ok=True)

    # Mendapatkan daftar file di dalam folder input
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # Baca gambar
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        # Lakukan blur pada gambar
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))

        # Simpan hasil di folder output
        output_path = os.path.join(output_folder, f"blurred_{image_file}")
        blurred_image.save(output_path)

if __name__ == "__main__":
    # Tentukan folder input, folder output, dan radius blur
    input_folder = "sample"
    output_folder = "output_blurred_pillow"
    blur_radius = 5  # Sesuaikan dengan kebutuhan Anda

    # Panggil fungsi untuk melakukan blur
    blur_images(input_folder, output_folder, blur_radius)

    print(f"Proses blur selesai. Hasil disimpan di folder '{output_folder}'.")
