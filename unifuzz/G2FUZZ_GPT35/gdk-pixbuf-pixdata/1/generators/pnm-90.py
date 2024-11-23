import os

def generate_pnm_file():
    content = """
    P3
    # This is a sample PNM file with additional features
    5 4
    255
    100 50 150   200 75 225   50 100 200   150 200 100  30 75 180
    200 75 225   100 50 150   75 225 100   200 200 50   80 120 200
    120 150 200   80 100 50   200 200 200   100 50 80   220 180 140
    30 75 180   80 100 50   200 200 200   100 50 80   220 180 140
    """
    with open("./tmp/example_extended.pnm", "w") as file:
        file.write(content)

if not os.path.exists("./tmp"):
    os.makedirs("./tmp")

generate_pnm_file()