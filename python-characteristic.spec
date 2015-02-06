%define	oname	characteristic

Name:		python2-%{oname}
Version:	14.3.0
Release:	2
Summary:	Python class decorators
Source0:	http://pypi.python.org/packages/source/c/%{oname}/%{oname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://github.com/hynek/characteristic/
BuildArch:	noarch
BuildRequires:	python2-setuptools

%description
``characteristic`` is an `MIT -licensed Python 
package with class decorators that ease 
the chores of implementing the most common 
attribute-related object protocols.
You just specify the attributes to work with and 
``characteristic`` gives you:
- a nice human-readable ``__repr__``,
- a complete set of comparison methods,
- and a kwargs-based initializer (that
cooperates with your existing one)
*without* writing dull boilerplate code again and again.



%prep
%setup -q -n %{oname}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc AUTHORS.rst
%doc LICENSE
%doc README.rst
%{py2_puresitedir}/characteristic.py*
%{py2_puresitedir}/test_characteristic.py*
%{py2_puresitedir}/characteristic*.egg-info
