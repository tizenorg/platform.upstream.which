Name:           which
Version:        2.20
Release:        4
License:        GPL-3.0
Summary:        Displays where a particular program in your path is located
Url:            http://www.xs4all.nl/~carlo17/which/
Group:          Applications/System
Source0:        http://www.xs4all.nl/~carlo17/which/%{name}-%{version}.tar.gz
BuildRequires:  readline-devel

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
