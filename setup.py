from distutils.core import setup
setup(
  name = 'ReflectionHelper',
  packages = ['ReflectionHelper'],
  version = '1.0',
  license='MIT',
  description = 'A reflection module based on the C# System.Reflection library',
  author = 'Qkrisi',
  author_email = 'qruczkristof@gmail.com',
  url = 'https://github.com/Qkrisi/ReflectionHelper',
  download_url = 'https://github.com/Qkrisi/ReflectionHelper/archive/v_1_0.tar.gz',
  keywords = ['Reflection', 'Helper'],
  install_requires=
			'forbiddenfruit',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
