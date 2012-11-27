Summary: Displays where a particular program in your path is located
Name: which
Version: 2.20
Release: 4
License: GPLv3
Group: Applications/System
Source0: http://www.xs4all.nl/~carlo17/which/%{name}-%{version}.tar.gz
Url: http://www.xs4all.nl/~carlo17/which/
BuildRequires: readline-devel

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%defattr(-,root,root)
%license COPYING 
%{_bindir}/*
