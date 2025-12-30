Summary:	A friend to fetch your data files
Name:		python-pooch
Version:	1.8.2
Release:	3
Group:		Development/Python
License:	MIT and Public Domain and APAFML and BSD and (ASL 2.0 and MIT)
URL:		https://github.com/pdfminer/pdfminer.six
#Source0:	https://github.com/fatiando/pooch/archive/v%{version}/pooch-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/p/pooch/pooch-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
Pooch manages your Python library's sample data files: it automatically
downloads and stores them in a local directory, with support for versioning
and corruption checks.

%files
%license LICENSE.txt
%doc README.md AUTHORS.md CITATION.rst CODE_OF_CONDUCT.md CONTRIBUTING.md
%{python3_sitelib}/pooch
%{py_puresitedir}/pooch-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n pooch-%{version}

%build
%py_build

%install
%py_install

