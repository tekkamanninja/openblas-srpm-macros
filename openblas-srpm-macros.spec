Name:           openblas-srpm-macros
Version:        2
Release:        1%{?dist}
Summary:        OpenBLAS architecture macros
Group:          Development/Libraries
License:        MIT
Source0:        macros.openblas-srpm
BuildArch:      noarch

%description
%{summary}.


%prep


%build


%install
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
mkdir -p %{buildroot}%{macrosdir}
install -m0644 %SOURCE0 %{buildroot}%{macrosdir}/macros.openblas-srpm


%files
%{macrosdir}/macros.openblas-srpm


%changelog
* Mon May 29 2017 Dan Horák <dan[at]danny.cz> - 2-1
- add s390x to supported arches

* Mon Mar 20 2017 Orion Poplawski <orion@cora.nwra.com> - 1-1
- Initial package
