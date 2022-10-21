import json
from opentrons import protocol_api, types


TEST_TIPRACK_SLOT = '5'

RATE = 0.25  # % of default speeds
SLOWER_RATE = 0.1

PIPETTE_MOUNT = 'right'
PIPETTE_NAME = 'p300_single_gen2'


TIPRACK_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"TipOne","brandId":["StarLab"]},"metadata":{"displayName":"TipOne 96 Tip Rack 300 µL","displayCategory":"tipRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.48,"zDimension":61},"wells":{"A1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":74.24,"z":8},"B1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":65.24,"z":8},"C1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":56.24,"z":8},"D1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":47.24,"z":8},"E1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":38.24,"z":8},"F1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":29.24,"z":8},"G1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":20.24,"z":8},"H1":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":14.38,"y":11.24,"z":8},"A2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":74.24,"z":8},"B2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":65.24,"z":8},"C2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":56.24,"z":8},"D2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":47.24,"z":8},"E2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":38.24,"z":8},"F2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":29.24,"z":8},"G2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":20.24,"z":8},"H2":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":23.38,"y":11.24,"z":8},"A3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":74.24,"z":8},"B3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":65.24,"z":8},"C3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":56.24,"z":8},"D3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":47.24,"z":8},"E3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":38.24,"z":8},"F3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":29.24,"z":8},"G3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":20.24,"z":8},"H3":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":32.38,"y":11.24,"z":8},"A4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":74.24,"z":8},"B4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":65.24,"z":8},"C4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":56.24,"z":8},"D4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":47.24,"z":8},"E4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":38.24,"z":8},"F4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":29.24,"z":8},"G4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":20.24,"z":8},"H4":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":41.38,"y":11.24,"z":8},"A5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":74.24,"z":8},"B5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":65.24,"z":8},"C5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":56.24,"z":8},"D5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":47.24,"z":8},"E5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":38.24,"z":8},"F5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":29.24,"z":8},"G5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":20.24,"z":8},"H5":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":50.38,"y":11.24,"z":8},"A6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":74.24,"z":8},"B6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":65.24,"z":8},"C6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":56.24,"z":8},"D6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":47.24,"z":8},"E6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":38.24,"z":8},"F6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":29.24,"z":8},"G6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":20.24,"z":8},"H6":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":59.38,"y":11.24,"z":8},"A7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":74.24,"z":8},"B7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":65.24,"z":8},"C7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":56.24,"z":8},"D7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":47.24,"z":8},"E7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":38.24,"z":8},"F7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":29.24,"z":8},"G7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":20.24,"z":8},"H7":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":68.38,"y":11.24,"z":8},"A8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":74.24,"z":8},"B8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":65.24,"z":8},"C8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":56.24,"z":8},"D8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":47.24,"z":8},"E8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":38.24,"z":8},"F8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":29.24,"z":8},"G8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":20.24,"z":8},"H8":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":77.38,"y":11.24,"z":8},"A9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":74.24,"z":8},"B9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":65.24,"z":8},"C9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":56.24,"z":8},"D9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":47.24,"z":8},"E9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":38.24,"z":8},"F9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":29.24,"z":8},"G9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":20.24,"z":8},"H9":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":86.38,"y":11.24,"z":8},"A10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":74.24,"z":8},"B10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":65.24,"z":8},"C10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":56.24,"z":8},"D10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":47.24,"z":8},"E10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":38.24,"z":8},"F10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":29.24,"z":8},"G10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":20.24,"z":8},"H10":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":95.38,"y":11.24,"z":8},"A11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":74.24,"z":8},"B11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":65.24,"z":8},"C11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":56.24,"z":8},"D11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":47.24,"z":8},"E11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":38.24,"z":8},"F11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":29.24,"z":8},"G11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":20.24,"z":8},"H11":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":104.38,"y":11.24,"z":8},"A12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":74.24,"z":8},"B12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":65.24,"z":8},"C12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":56.24,"z":8},"D12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":47.24,"z":8},"E12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":38.24,"z":8},"F12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":29.24,"z":8},"G12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":20.24,"z":8},"H12":{"depth":53,"totalLiquidVolume":300,"shape":"circular","diameter":5,"x":113.38,"y":11.24,"z":8}},"groups":[{"metadata":{},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":true,"tipLength":53,"isMagneticModuleCompatible":false,"loadName":"tipone_96_tiprack_300ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
TIPRACK_DEF = json.loads(TIPRACK_DEF_JSON)
TIPRACK_LABEL = TIPRACK_DEF.get('metadata', {}).get(
    'displayName', 'test labware')

metadata = {'apiLevel': '2.0'}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware_from_definition(TIPRACK_DEF, TEST_TIPRACK_SLOT, TIPRACK_LABEL)
    pipette = protocol.load_instrument(
        PIPETTE_NAME, PIPETTE_MOUNT, tip_racks=[tiprack])

    num_cols = len(TIPRACK_DEF.get('ordering', [[]]))
    num_rows = len(TIPRACK_DEF.get('ordering', [[]])[0])


    def set_speeds(rate):
        protocol.max_speeds.update({
            'X': (600 * rate),
            'Y': (400 * rate),
            'Z': (125 * rate),
            'A': (125 * rate),
        })

        speed_max = max(protocol.max_speeds.values())

        for instr in protocol.loaded_instruments.values():
            instr.default_speed = speed_max

    set_speeds(RATE)
    firstwell = tiprack.well('A1')
    pipette.move_to(firstwell.top())
    protocol.pause("If the pipette is accurate click 'resume'")
    pipette.pick_up_tip()
    protocol.pause("If the pipette went into the center of the tip, click 'resume'")
    pipette.return_tip()
    protocol.pause("If the pipette successfully picked up the tip(s) but does not eject succesfully, pull the tip(s) off by hand and click 'resume'. Do not worry about tip ejection yet")

    last_col = (num_cols * num_rows) - num_rows
    if (PIPETTE_NAME == 'p20_multi_gen2' or PIPETTE_NAME == 'p300_multi_gen2'):
        well = tiprack.well(last_col)
        pipette.move_to(well.top())
        protocol.pause("If the position is accurate click 'resume'")
        pipette.pick_up_tip(well)
    else:
        last_well = (num_cols) * (num_rows)
        well = tiprack.well(last_well-1)
        pipette.move_to(well.top())
        protocol.pause("If the position is accurate click 'resume'")
        pipette.pick_up_tip(well)

    protocol.pause("If the pipette went to the center of the tip, click 'resume'")
    pipette.return_tip()
    protocol.comment("If the pipette successfully picked up the tip(s) but does not eject succesfully, pull the tip(s) off by hand and click 'resume'. Do not worry about tip ejection yet")

