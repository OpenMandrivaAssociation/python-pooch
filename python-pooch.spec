%define module pooch

Name:		python-pooch
Summary:	A friend to fetch your data files
Version:	1.9.0
Release:	1
Group:		Development/Python
License:	MIT and Public Domain and APAFML and BSD and (ASL 2.0 and MIT)
URL:		https://github.com/fatiando/pooch
Source0:	https://pypi.io/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Pooch manages your Python library's sample data files: it automatically
downloads and stores them in a local directory, with support for versioning
and corruption checks.

%files
%license LICENSE.txt
%doc README.md AUTHORS.md CITATION.rst CONTRIBUTING.md
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
