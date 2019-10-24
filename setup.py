import setuptools
import pkg_resources
import os
import shutil
from setuptools.command.install import install

package_name = "melopero-fan-hat"

class InstallCommand(install):
    def initialize_options(self):
        install.initialize_options(self)

    def finalize_options(self):
        #print('The custom option for install is ', self.custom_option)
        install.finalize_options(self)

    def run(self):
        install.run(self)  # OR: install.do_egg_install(self)
        
        #copy script inside autostart script folder
        fan_controller_path = os.path.abspath(pkg_resources.resource_filename(package_name, "fan_controller.py"))
        final_path = os.path.join("/home/melopero-autostart/scripts/", "fan_controller.py")
        shutil.copyfile(fan_controller_path, final_path)
        os.chmod(final_path, 0o664)    
        
        #copy uninstall script inside autostart uninstall scripts folder
        uninstall_script_path = os.path.abspath(pkg_resources.resource_filename(package_name, "uninstall_melopero_fan_hat.sh"))
        final_uninstall_path = os.path.join("/home/melopero-autostart/uninstall/uninstall-scripts/", "uninstall_melopero_fan_hat.sh")
        shutil.copyfile(uninstall_script_path, final_uninstall_path)
        os.chmod(final_uninstall_path, 0o554)

setuptools.setup(
    name="melopero_fan_hat",
    version="0.0.4",
    description="Melopero Fan Hat, automatically sets up your melopero-fan-hat",
    #url="https://github.com/melopero/Melopero_AMG8833/tree/master/module",
    author="Melopero",
    author_email="info@melopero.com",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires = ['melopero_autostart>=0.0.7', 'RPi.GPIO'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    cmdclass={
        'install': InstallCommand,
    },
)