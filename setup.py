from setuptools import setup

setup(name='rb-payment',
    version='0.1',
    description='a client lib for rb payment',
    author='Aman Srivastav',
    author_email='aman.srivastava@renewbuy.com',
    license='MIT',
    packages=['rb_payment'],
    # scripts=['bin/payment_tests.py'],
    zip_safe=False,
    install_requires=[
        'PyJWT',
        'requests'
    ],
)