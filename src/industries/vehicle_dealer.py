from industry import IndustryTertiary, TileLocationChecks

industry = IndustryTertiary(id='vehicle_dealer',
                            accept_cargo_types=['VEHI'],
                            prod_cargo_types=[],
                            prob_in_game='14',
                            prob_random='14',
                            prod_multiplier='[0, 0]',
                            map_colour='189',
                            life_type='IND_LIFE_TYPE_BLACK_HOLE',
                            spec_flags='bitmask(IND_FLAG_BUILT_NEAR_TOWN)',
                            location_checks=dict(same_type_distance=32),
                            prospect_chance='0.75',
                            name='string(STR_IND_VEHICLE_DEALER)',
                            nearby_station_name='string(STR_STATION_VEHICLE_DEALER)',
                            fund_cost_multiplier='8')

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='vehicle_dealer_tile_1',
                  location_checks=TileLocationChecks(
                      require_road_adjacent=True,
                      require_effectively_flat=True))

spriteset_ground = industry.add_spriteset(
    type='concrete',
)
spriteset_ground_overlay = industry.add_spriteset(
    type='empty'
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 59, -31, -28)]
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 59, -31, -28)]
)

industry.add_spritelayout(
    id='vehicle_dealer_spritelayout_1',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='vehicle_dealer_spritelayout_2',
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=['nw', 'ne', 'se', 'sw']
)

industry.add_industry_layout(
    id='vehicle_dealer_industry_layout_1',
    layout=[(0, 0, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_1'),
            (0, 1, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_2')
            ]
)
industry.add_industry_layout(
    id='vehicle_dealer_industry_layout_2',
    layout=[(0, 0, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_1'),
            (1, 0, 'vehicle_dealer_tile_1', 'vehicle_dealer_spritelayout_2')
            ]
)
