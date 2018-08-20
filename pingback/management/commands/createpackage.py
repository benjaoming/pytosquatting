import os
import subprocess
import tempfile
from django.core.management.base import BaseCommand


from pingback import models


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('package_name',
                            help="Name of package to create")
        # parser.add_argument('owner',
        #                     help="Name of the person/bot who created this")
        # parser.add_argument('--url',
        #                     default=False,
        #                     help="Some option")

    def handle(self, *args, **options):
        """gets data from WordPress site"""
        package_name = options['package_name']
        output_dir = tempfile.mkdtemp()
        
        template_dir = os.path.join(
            os.path.dirname(__file__), 'data', 'pypi_template'
        )
        setup_py = open(os.path.join(template_dir, 'setup.py'), 'r').read()
        readme_rst = open(os.path.join(template_dir, 'README.rst'), 'r').read()
        
        setup_py = setup_py.replace('{{ PACKAGE_NAME }}', package_name)
        readme_rst = readme_rst.replace('{{ PACKAGE_NAME }}', package_name)
        
        open(os.path.join(output_dir, 'setup.py'), 'w').write(setup_py)
        open(os.path.join(output_dir, 'README.rst'), 'w').write(readme_rst)
        
        subprocess.call(
            ['python', 'setup.py', 'sdist'],
            cwd=output_dir
        )

        subprocess.call(
            ['twine', 'upload', 'dist/*'],
            cwd=output_dir
        )

        models.Pingback.objects.get_or_create(repository="pypi", package_name=package_name)
        
        print("Creating package in {}".format(output_dir))
