Name:           deepin-clone
Version:        5.0.3
Release:        2
Summary:        Disk and partition backup/restore tool
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-clone
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         modify-QPainterPath-error.patch

BuildRequires:  gcc-c++ desktop-file-utils qt5-linguist qt5-qtbase-private-devel
BuildRequires:  dtkwidget2-devel dtkcore2-devel deepin-gettext-tools dtkcore2 dtkwidget2 
BuildRequires:  pkgconfig(polkit-qt5-1) pkgconfig(Qt5Core) pkgconfig(Qt5Concurrent) pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       hicolor-icon-theme partclone
ExclusiveArch:  x86_64 %{ix86} aarch64

%description
%{summary}.

%prep
%autosetup -p1
sed -i 's|/usr/sbin|/usr/bin|' app/{%{name}-app.pro,%{name}-ionice,%{name}-pkexec,com.deepin.pkexec.%{name}.policy.tmp}

%build
export PATH=%{_qt5_bindir}:$PATH
export CFLAGS="%{optflags} -Wno-error=format-security"
export CXXFLAGS="%{optflags} -Wno-error=format-security"
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/polkit-1/actions//com.deepin.pkexec.%{name}.policy

%changelog
* Thu Feb 10 2022 liweigang <liweiganga@uniontech.com> - 5.0.3-2
- fix build error

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 5.0.3-1
- Initial build
