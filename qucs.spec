Summary:	An integrated circuit simulator
Name:		qucs
Version:	0.0.16
Release:	%mkrel 1
License:	QPL
Group:		Sciences/Other
URL:		http://qucs.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		qucs-0.0.16-format_string_fixes.diff
BuildRequires:	flex, bison, qt3-devel, imagemagick
%description
Qucs is going to be an integrated circuit simulator which means you will be
able to setup a circuit with a graphical user interface (GUI) and simulate the 
large-signal, small-signal and noise behaviour of the circuit. After that 
simulation has finished you can present the simulation results on a 
presentation page or window.

%prep

%setup -q
%patch0 -p1

%build

export QTDIR=%{qt3dir}
export PATH=$PATH:%{qt3bin}

perl -pi -e 's|/usr/local/qt/lib|%{qt3lib}|' configure*
perl -pi -e 's|/usr/local/qt/include|%{qt3include}|' configure*

%configure_qt3
%make

%install

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

%files
%doc README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
%{_iconsdir}/%{iconname}
%{_miconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_datadir}/applications/*
