import io
from pathlib import Path

from PIL import Image

valid_mock_access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMSwiZW1haWwiOiJUZXN0QGdtYWlsLmNvbSIsInJvbGUiOiJ1c2VyIiwiZXhwIjo0ODgxMTI0NjY1fQ.pyN38WUX_zguzaAyeivC0YLv7Rsxz-nDaVdFCeEnG2w'
valid_mock_refresh_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMSwiZXhwIjo0ODgxMTI0NjY1fQ.EPcUZfakItrjDfHtbrnIX2d9BSLnJPSvx-Pv7U4ODkI'
invalid_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
expenditures_mock_data = [('Dairy',17.82),('Animal',16.62),('Beverages',10.95),('Fruit',4),('Pastries',3.38)]
large_mock_file = {'image': ('large_image.jpg', io.BytesIO( b'x' * (5 * 1024 * 1024)), 'image/jpeg')}
small_mock_file =  {'image': ('large_image.jpg', io.BytesIO( b'x' * (1 * 1024 * 1024)), 'image/jpeg')}
invalid_mock_file = {'image': ('large_image.jpg', io.BytesIO( b'x' * (1 * 1024 * 1024)), 'image/webp')}