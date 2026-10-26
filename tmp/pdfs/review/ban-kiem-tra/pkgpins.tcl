create_project -in_memory -part xc7a35tfgg484-2
set_property DESIGN_MODE PinPlanning [current_fileset]
open_io_design -name io_1
set f [open pkgpins.csv w]
puts $f "pin,bank,func"
foreach p [get_package_pins] {
  puts $f "[get_property NAME $p],[get_property BANK $p],[get_property PIN_FUNC $p]"
}
close $f
puts "DONE"
