#
# spec file for package python-pyscard
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2011 LISA GmbH, Bingen, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define python_version python3
%bcond_without test
%define modname pyscard
Name:           python3-pyscard
Version:        2.0.0
Release:        0
Summary:        Python module adding smart card support
License:        LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://pyscard.sourceforge.net/
# Source:         https://files.pythonhosted.org/packages/source/p/pyscard/pyscard-%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-rpm-macros
BuildRequires:  swig
Requires:       pcsc-ccid


%description
Python-pyscard consists of smartcard.scard, an extension module wrapping
Windows smart card base components (also known as PCSC) on Windows and PCSC
lite on linux and Mac OS X Tiger and Leopard, and smartcard, a higher level
python framework built on top of the raw PCSC API.

%prep
%setup -q -n %{name}-%{version}/pyscard
mv smartcard/doc .

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%{_libdir}/%{python_version}.*/site-packages/pyscard-%{version}-*
%{_libdir}/%{python_version}.*/site-packages/smartcard/*


%doc ChangeLog doc README.md
%license LICENSE
%{python3_sitearch}/*

%changelog
