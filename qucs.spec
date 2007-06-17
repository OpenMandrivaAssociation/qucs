%define name qucs
%define version 0.0.9
%define release %mkrel 1

Summary: An integrated circuit simulator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: QPL
Group: Sciences/Other
Url: http://qucs.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: flex, bison, qt3-devel

%description
Qucs is going to be an integrated circuit simulator which means you will be
able to setup a circuit with a graphical user interface (GUI) and simulate the 
large-signal, small-signal and noise behaviour of the circuit. After that 
simulation has finished you can present the simulation results on a 
presentation page or window.

%prep
%setup -q 
%build

export PATH=$PATH:$QTDIR/bin

perl -pi -e 's|/usr/local/qt/lib|\$QTDIR/%{_lib}|' configure
%configure 
%make

%install
rm -rf %{buildroot}
%makeinstall

# add menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/%{name}"\
needs="x11" \
section="More Applications/Sciences/Electricity"\
title="Qucs"\
icon="electricity_section.png"\
longtitle="Simulate electrical circuits"
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README

%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_menudir}/%{name}
