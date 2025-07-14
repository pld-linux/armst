Summary:	ST ARM-CortexM3 Linux RS-232 Loader
Summary(pl.UTF-8):	Programator RS-232 dla ST ARM-CortexM3 
Name:		armst
Version:	1.20
Release:	1
License:	GPL v3
Group:		Development/Tools
Source0:	http://isotel.eu/ARMst/%{name}-%{version}-src.tgz
# Source0-md5:	aeaf4fa71c5b2cf7a4678409f82ec13e
Patch0:		stmbl.patch
URL:		http://isotel.eu/ARMst/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The ARMst utility is a command line tool for flashing the ST
ARM-CortexM3 family via the standard RS-232 port.

%description -l pl.UTF-8
ARMst jest narzędziem konsolowym do programowania pamięci flash
mikrokontrolerów ST ARM Cortex-M3 przy użyciu portu RS-232.

%prep
%setup -n ARMst -q
%patch -P0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LIBS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/armst
