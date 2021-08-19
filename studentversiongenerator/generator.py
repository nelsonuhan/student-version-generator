import argparse
import os.path
from traitlets.config import Config
from nbconvert.exporters import NotebookExporter
from nbconvert.preprocessors import ClearOutputPreprocessor, TagRemovePreprocessor


def create_student_version(input_filename):
    c = Config()

    c.ClearOutputPreprocessor.enabled = True

    c.TagRemovePreprocessor.remove_cell_tags = ("solution",)
    c.TagRemovePreprocessor.enabled = True

    c.NotebookExporter.preprocessors = [
        'nbconvert.preprocessors.ClearOutputPreprocessor',
        'nbconvert.preprocessors.TagRemovePreprocessor'
    ]

    exporter = NotebookExporter(config=c)
    exporter.register_preprocessor(ClearOutputPreprocessor(config=c), True)
    exporter.register_preprocessor(TagRemovePreprocessor(config=c), True)

    abs_input_filename = os.path.abspath(input_filename)
    abs_input_basename = os.path.splitext(abs_input_filename)[0]
    abs_output_filename = f'{abs_input_basename} student.ipynb'

    output = exporter.from_filename(abs_input_filename)

    with open(abs_output_filename, 'w') as f:
        f.write(output[0])


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Notebook with solutions')
    args = parser.parse_args(argv)
    create_student_version(args.filename)
