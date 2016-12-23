#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-barbicanclient
Version  : 4.1.0
Release  : 26
URL      : http://tarballs.openstack.org/python-barbicanclient/python-barbicanclient-4.1.0.tar.gz
Source0  : http://tarballs.openstack.org/python-barbicanclient/python-barbicanclient-4.1.0.tar.gz
Summary  : Client Library for OpenStack Barbican Key Management API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-barbicanclient-bin
Requires: python-barbicanclient-python
BuildRequires : Jinja2
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : hacking
BuildRequires : msgpack-python-python
BuildRequires : nose-python
BuildRequires : openstacksdk-python
BuildRequires : oslo.config
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyparsing-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-cinderclient-python
BuildRequires : python-dev
BuildRequires : python-glanceclient-python
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock-python
BuildRequires : python-novaclient-python
BuildRequires : python-openstackclient-python
BuildRequires : python3-dev
BuildRequires : requests-mock-python
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
python-barbicanclient
=====================
.. image:: https://img.shields.io/pypi/v/python-barbicanclient.svg
:target: https://pypi.python.org/pypi/python-barbicanclient/
:alt: Latest Version

%package bin
Summary: bin components for the python-barbicanclient package.
Group: Binaries

%description bin
bin components for the python-barbicanclient package.


%package python
Summary: python components for the python-barbicanclient package.
Group: Default
Requires: cliff-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: python-keystoneclient-python

%description python
python components for the python-barbicanclient package.


%prep
%setup -q -n python-barbicanclient-4.1.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/barbican

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
