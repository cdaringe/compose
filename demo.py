from compose.cli.docopt_command import DocoptDispatcher
from compose.cli.command import project_from_options
from compose.cli.utils import get_version_info
from compose.cli.main import TopLevelCommand
from compose.service import ImageType

import time

project_dir = '.'

dispatcher = DocoptDispatcher(
    TopLevelCommand,
    {
      'options_first': True,
      'version': get_version_info('compose')
    }
)

options, handler, command_options = dispatcher.parse(['up']) # use 'up' to get initial options
project = project_from_options(project_dir, options)

for service in project.services:
  service.start()
  lbl_str = ', '.join(service.labels())
  img_name = service.image_name
  print(f'service image: {img_name} {lbl_str}')
time.sleep(4)
# down(remove_image_type, include_volumes, remove_orphans=False, timeout=None, ignore_orphans=False)
project.down(ImageType.none, include_volumes=False, remove_orphans=True)
