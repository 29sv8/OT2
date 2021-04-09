// @flow
import * as React from 'react'
import cx from 'classnames'

import { PIPETTE_MOUNTS } from '../../pipettes'
import { InstrumentGroup } from '@opentrons/components'
import styles from './styles.css'

import type { InstrumentInfoProps } from '@opentrons/components'
import type { Pipette, Labware } from '../../robot/types'
import type { Mount } from '../../pipettes/types'

export type PipettesProps = {|
  currentMount: Mount | null,
  pipettes: Array<Pipette>,
  activeTipracks: {| left: Labware | null, right: Labware | null |},
  changePipetteUrl: string,
|}

export function Pipettes(props: PipettesProps): React.Node {
  const { currentMount, pipettes, activeTipracks } = props

  const infoByMount = PIPETTE_MOUNTS.reduce<
    $Shape<{|
      left?: InstrumentInfoProps,
      right?: InstrumentInfoProps,
    |}>
  >((result, mount) => {
    const pipette = pipettes.find(p => p.mount === mount)
    const tiprack = activeTipracks[mount]
    const pipetteConfig = pipette?.modelSpecs
    const isDisabled = !pipette || mount !== currentMount

    const details = !pipetteConfig
      ? { description: 'N/A', tiprackModel: 'N/A' }
      : {
          description: pipetteConfig.displayName,
          tiprackModel:
            tiprack?.definition?.metadata.displayName || tiprack?.name || 'N/A',
          pipetteSpecs: pipetteConfig,
        }

    result[mount] = {
      mount,
      isDisabled,
      className: cx(styles.instrument, styles[mount]),
      infoClassName: styles.instrument_info,
      ...details,
    }

    return result
  }, {})

  return <InstrumentGroup {...infoByMount} />
}
