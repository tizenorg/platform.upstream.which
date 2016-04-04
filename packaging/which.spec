Name:           which
Version:        2.20
Release:        4
License:        GPL-3.0
Summary:        Displays where a particular program in your path is located
Url:            http://www.xs4all.nl/~carlo17/which/
Group:          Applications/System
Source0:        http://www.xs4all.nl/~carlo17/which/%{name}-%{version}.tar.bz2
Source1001: 	which.manifest
BuildRequires:  readline-devel

%description
The which command shows the full pathname of a specified program, if
the specified program is in your PATH.

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
%configure

make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/*
