%define Werror_cflags %{nil}

# %define svn 1842

Summary:	An integrated circuit simulator
Name:		qucs
Version:	0.0.17
Release:	1
License:	QPL
Group:		Sciences/Other
Url:		http://qucs.sourceforge.net/
Source0:	%{name}-%{version}.tar.gz
Patch0:		qucs-0.0.17-format-security.patch
BuildRequires:	adms
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	qt4-devel
BuildRequires:	imagemagick

%description
Qucs is going to be an integrated circuit simulator which means you will be
able to setup a circuit with a graphical user interface (GUI) and simulate the
large-signal, small-signal and noise behaviour of the circuit. After that
simulation has finished you can present the simulation results on a
presentation page or window.

%prep
%setup -q
%apply_patches

%build
autoreconf -vfi
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_miconsdir} %{buildroot}%{_iconsdir} %{buildroot}%{_liconsdir}
convert -resize 16x16 qucs/bitmaps/ysmith.png %{buildroot}%{_miconsdir}/%{name}.png
convert -resize 32x32 qucs/bitmaps/ysmith.png %{buildroot}%{_iconsdir}/%{name}.png
convert -resize 48x48 qucs/bitmaps/ysmith.png %{buildroot}%{_liconsdir}/%{name}.png
chmod 644 %{buildroot}%{_miconsdir}/%{name}.png
chmod 644 %{buildroot}%{_iconsdir}/%{name}.png
chmod 644 %{buildroot}%{_liconsdir}/%{name}.png

# add menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=An integrated circuit simulator
Comment[ru]=Симулятор электрических цепей
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
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


