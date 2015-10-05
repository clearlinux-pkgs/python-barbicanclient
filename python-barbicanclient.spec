#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-barbicanclient
Version  : 3.3.0
Release  : 15
URL      : http://tarballs.openstack.org/python-barbicanclient/python-barbicanclient-3.3.0.tar.gz
Source0  : http://tarballs.openstack.org/python-barbicanclient/python-barbicanclient-3.3.0.tar.gz
Summary  : Client Library for OpenStack Barbican Key Management API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-barbicanclient-bin
Requires: python-barbicanclient-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : nose-python
BuildRequires : oslo.config
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests
BuildRequires : requests-mock-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
python-barbicanclient
=====================
This is a client for the `Barbican <https://github.com/openstack/barbican>`__
Key Management API.  There is a Python library for accessing the API
(`barbicanclient` module), and a command-line script (`barbican`).

%package bin
Summary: bin components for the python-barbicanclient package.
Group: Binaries

%description bin
bin components for the python-barbicanclient package.


%package python
Summary: python components for the python-barbicanclient package.
Group: Default
Requires: cliff-python
Requires: oslo.i18n-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: python-keystoneclient-python

%description python
python components for the python-barbicanclient package.


%prep
%setup -q -n python-barbicanclient-3.3.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test || :
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
