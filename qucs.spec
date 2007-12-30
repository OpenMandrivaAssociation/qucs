%define name 		qucs
%define version 	0.0.13
%define release 	%mkrel 1
%define Summary		An integrated circuit simulator

Summary: 			%{Summary}
Name: 				%{name}
Version:			%{version}
Release: 			%{release}
Source0: 			%{name}-%{version}.tar.gz
License: 			QPL
Group: 				Sciences/Other
Url: http://qucs.sourceforge.net/
BuildRequires: flex, bison, qt3-devel, ImageMagick

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

%define button qucs/bitmaps/ysmith.png
%define iconname %{name}.png
mkdir -p %{buildroot}%{_miconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_liconsdir}
convert -resize 16x16 %{button} %{buildroot}%{_miconsdir}/%{iconname}
convert -resize 32x32 %{button} %{buildroot}%{_iconsdir}/%{iconname}
convert -resize 48x48 %{button} %{buildroot}%{_liconsdir}/%{iconname}
chmod 644 %{buildroot}%{_miconsdir}/%{iconname}
chmod 644 %{buildroot}%{_iconsdir}/%{iconname}
chmod 644 %{buildroot}%{_liconsdir}/%{iconname}

# add menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/%{name}"\
needs="x11" \
section="More Applications/Sciences/Electricity"\
title="Qucs"\
icon="%{iconname}"\
longtitle="Simulate electrical circuits"\
xdg="true"
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Electricity;Science;X-MandrivaLinux-MoreApplications-Sciences-Electricity;
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
%{_iconsdir}/%{iconname}
%{_miconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_datadir}/applications/*

