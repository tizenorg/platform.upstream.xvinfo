%bcond_with x

Summary: Print out X-Video extension adaptor information
Name: xvinfo
Version: 1.1.2
Release: 1
License: MIT
Group: User Interface/X
URL: http://www.x.org
Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(dmx) pkgconfig(xext) pkgconfig(xft) pkgconfig(xrandr)
BuildRequires: pkgconfig(xi) pkgconfig(xinerama) pkgconfig(xmu)
BuildRequires: pkgconfig(xpm) pkgconfig(xt) pkgconfig(xtst) pkgconfig(xv)
BuildRequires: pkgconfig(xxf86dga) pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-atom)

%if !%{with x}
ExclusiveArch:
%endif

%description
Prints  out the capabilities of any video adaptors associated with the
display that are accessible through the X-Video extension.

%prep
%setup -q

%build
%autogen --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
{
      make install DESTDIR=$RPM_BUILD_ROOT
}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc
%{_bindir}/*
#%{_bindir}/xvinfo
#%{_mandir}/man1/xvinfo.1*
