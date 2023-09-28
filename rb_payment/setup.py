from setuptools import setup

setup(name='py_qbee_tst',
    version='0.1',
    description='test package to run on qbee.io',
    author='qbee AS',
    author_email='author@somemail.com',
    license='MIT',
    packages=['rb_payment'],
    # scripts=['bin/payment_tests.py'],
    zip_safe=False,
    install_requires=[
        'PyJWT',
        'requests'
    ],
)