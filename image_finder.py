import os

image_extensions = [
    # Common Raster Image Formats
    "jpg", "jpeg", "jpe", "jif", "jfif", "jfi",  # JPEG-based formats
    "png",  # PNG
    "gif",  # GIF
    "bmp", "dib",  # BMP
    "tiff", "tif",  # TIFF
    "webp",  # WEBP
    "heif", "heic",  # HEIF/HEIC
    "ico",  # ICO (Icon)
    "cur",  # CUR (Cursor)
    "tga", "icb", "vda", "vst",  # TGA (Targa)
    "pcx",  # PCX
    "pnm", "pbm", "pgm", "ppm",  # PNM Formats

    # Raw Image Formats (Camera Raw)
    "crw", "cr2", "cr3",  # Canon RAW
    "nef", "nrw",  # Nikon RAW
    "arw", "srf", "sr2",  # Sony RAW
    "raf",  # Fuji RAW
    "orf",  # Olympus RAW
    "rw2", "raw",  # Panasonic RAW
    "dcr", "kdc", "dc2",  # Kodak RAW
    "rwl",  # Leica RAW
    "pef",  # Pentax RAW
    "x3f",  # Sigma RAW
    "erf",  # Epson RAW
    "iiq",  # Phase One RAW

    # Vector Image Formats
    "svg", "svgz",  # SVG
    "ai",  # Adobe Illustrator
    "cdr",  # CorelDRAW
    "eps",  # Encapsulated PostScript
    "wmf", "emf",  # Windows Metafile
    "xar",  # Xara Vector Format

    # 3D & Specialized Image Formats
    "3dm", "3ds", "dae", "obj", "stl",  # 3D Image Formats
    "hdr", "exr",  # HDR Formats
    "dcm",  # DICOM (Medical Imaging)
    "djvu",  # Portable Document Image
    "jxl",  # JPEG XL

    # Other Miscellaneous Formats
    "psd",  # Photoshop Document Format
    "xcf",  # GIMP Image Format
    "xbm", "xpm",  # X Windows Bitmap Formats
    "iff", "lbm",  # Amiga Formats
    "pict", "qtif",  # Apple Formats
    "hdp", "jxr",  # Microsoft Image Formats
]

a=''
def generator():
    for dirpath, dirnames, filenames in os.walk("C:\\Users\\kamal\\Desktop\\react"):
        yield(dirpath)
        yield(dirnames)
        yield(filenames)




gen = generator()
gent = str(next(gen))
print(gent, type(gent))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

    

    


