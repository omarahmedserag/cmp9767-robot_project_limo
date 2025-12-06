from setuptools import setup

package_name = 'perception'

setup(
    name=package_name,
    version='0.0.0',
    py_modules=['detector'],  # ← because detector.py is directly in src/perception/
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Omar Seraj',
    maintainer_email='omarseraj17@gmail.com',
    description='Color detection node for LIMO',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'detector = detector:main',  # ← module = detector.py, function = main()
        ],
    },
)