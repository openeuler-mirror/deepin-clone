Name:           deepin-clone
Version:        5.0.11
Release:        1
Summary:        Disk and partition backup/restore tool
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-clone
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkcore-devel
BuildRequires:  dtkgui-devel
BuildRequires:  deepin-gettext-tools
BuildRequires:  dde-file-manager-devel

%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       hicolor-icon-theme
Requires:       partclone
Requires:       jfsutils
Requires:       ntfs-3g
Requires:       xfsprogs
ExclusiveArch:  x86_64 %{ix86} aarch64

%description
%{summary}.

%prep
%autosetup -p1
sed -i 's|sbin|bin|' CMakeLists.txt
sed -i 's|Version=0.1|Version=%{version}|' app/%{name}.desktop
#sed -i 's|/usr/sbin|/usr/bin|' app/{%{name}-app.pro,%{name}-ionice,%{name}-pkexec,com.deepin.pkexec.%{name}.policy.tmp}

%build
export PATH=%{_qt5_bindir}:$PATH
export CFLAGS="%{optflags} -Wno-error=format-security"
export CXXFLAGS="%{optflags} -Wno-error=format-security"
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
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
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/polkit-1/actions//com.deepin.pkexec.%{name}.policy
%{_libdir}/dde-file-manager/plugins/controllers/libdfm-plugin-dim-file.so

%changelog
* Thu Jun 01 2023 leeffo <liweiganga@uniontech.com> - 5.0.11-1
- update to 5.0.11

* Thu Feb 10 2022 liweigang <liweiganga@uniontech.com> - 5.0.3-2
- fix build error

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 5.0.3-1
- Initial build
