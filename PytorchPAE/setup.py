from setuptools import setup

setup(name='pytorch_pae',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='a pytorch package for training a probabilistic autoencoder',
      url='https://github.com/Aurora-Xiang/ML-for-Quasar-Classification/tree/main/PytorchPAE',
      author='Xiang Chen',
      author_email='auroracx0128@gmail.com',
      license='MIT',
      packages=['pytorch_pae']
      )
